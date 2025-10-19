```json
{
  "id": "16842e5ce9746629",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294787,
  "host_pid": "9e6742732c60:1",
  "hash": "9cd379f3e45a5903d34d56da1fc1b7526025856d8c2129d709064746ab50029e",
  "cid": "QmV19cd379f3e45a5903d34d56da1fc1b7526025856d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294787,
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
      "evaluated_at": 1760294787
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "a45181ae69241fe43afdb7c6c5191f90b2322fadebccc3d21df88e253810204c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025503816
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 95696800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': 'fc6cd7074b4844e3'}}}