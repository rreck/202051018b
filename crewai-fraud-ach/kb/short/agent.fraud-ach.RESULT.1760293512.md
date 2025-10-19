```json
{
  "id": "b29c7e2ae7ba9604",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293512,
  "host_pid": "9e6742732c60:1",
  "hash": "b238c48a5b32b693d19b7faba00f18d6c791d95983b219e302783e8ca7939f24",
  "cid": "QmV1b238c48a5b32b693d19b7faba00f18d6c791d959",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293512,
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
      "evaluated_at": 1760293512
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
  "sig": "c926b64bc4a3df58919fb946a70db2cecc4dcfe1f27c154d126e1c2e4c868df9"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 244163284273009
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 72863560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '5b6cb55161b8e1f8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '244163284', 'validation_error': 'Invalid routing number checksum'}}}