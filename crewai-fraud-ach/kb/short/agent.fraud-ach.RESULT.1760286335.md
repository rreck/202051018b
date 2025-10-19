```json
{
  "id": "6ed7c16e7dbfd7fd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286335,
  "host_pid": "9e6742732c60:1",
  "hash": "4124a18f9f1e5903155063d097b2ff0c5a1c25713d7804c712b66ca2dffb8a8f",
  "cid": "QmV14124a18f9f1e5903155063d097b2ff0c5a1c2571",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286335,
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
      "evaluated_at": 1760286335
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "6684a110315e09fbd85e1247bb71a88e9dc1b68cbf83a5eaaba7c174d2f406cf"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 122105158962917
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 22000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 21, 'first_seen': 1760285763, 'matching_hash': '11dc2cfd2eb8ef5d'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}