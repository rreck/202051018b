```json
{
  "id": "c374669e9d590879",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293517,
  "host_pid": "9e6742732c60:1",
  "hash": "f816972e104b2ab5230a3506a2cbad265d6890536308c5d81e10e6c33c0ff3b2",
  "cid": "QmV1f816972e104b2ab5230a3506a2cbad265d689053",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293517,
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
      "evaluated_at": 1760293517
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
  "sig": "e79de5bbc1855cfe7b37e86706a6803091c98292da31a38bc3c2b50a1dacff29"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271730017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 80252480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '5b0cb81735d50318'}}}