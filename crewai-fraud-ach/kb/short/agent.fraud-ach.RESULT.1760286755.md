```json
{
  "id": "b6f7229f979c58b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286755,
  "host_pid": "9e6742732c60:1",
  "hash": "3adbb82dc202c5d058f81fb95a884e966adbfc0a64ccf4e56cc0c6c4aee52bcf",
  "cid": "QmV13adbb82dc202c5d058f81fb95a884e966adbfc0a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286755,
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
      "evaluated_at": 1760286755
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
  "sig": "63934c292c1540e43419a59afed98621e13316303b0d7ff7bb6e910d3757e9bc"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 208726937303978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11953512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285763, 'matching_hash': '49fe8226d43b3ae7'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '208726934', 'validation_error': 'Invalid routing number checksum'}}}