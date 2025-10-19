```json
{
  "id": "d5b15f35887c03cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288304,
  "host_pid": "9e6742732c60:1",
  "hash": "4a8a64b2c222486f8c5218a34457bfee0830ebd5502c792d5d1d22549fc6aeb5",
  "cid": "QmV14a8a64b2c222486f8c5218a34457bfee0830ebd5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288304,
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
      "evaluated_at": 1760288304
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
  "sig": "b7621d925fb25ae575a4e6bccb47a2a294b4c01b43bf06aa49a6ff96010bc07e"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 537469236347495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 18842368, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285763, 'matching_hash': 'a49bc27baafeabf1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '537469236', 'validation_error': 'Invalid routing number checksum'}}}