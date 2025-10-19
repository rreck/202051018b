```json
{
  "id": "45053671a846bf81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286811,
  "host_pid": "9e6742732c60:1",
  "hash": "7c56ec6e5163881c5a95005457e5ea8fbbb9b39c27ca5a76b03435e6f7df4720",
  "cid": "QmV17c56ec6e5163881c5a95005457e5ea8fbbb9b39c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286811,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760286811
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "d72f2957ffe83bb17489a1dbbb7f6aee31799e48f1566002285ecd8dbfcc1f7d"
}
```

Fraud detected: invalid_routing (score: 90)
Transaction: 098545588857560
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285764, 'matching_hash': '7b745f55cd5357b8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}: True, 'risk_score': 95, 'details': {'routing_number': '113877666', 'validation_error': 'Invalid routing number checksum'}}}