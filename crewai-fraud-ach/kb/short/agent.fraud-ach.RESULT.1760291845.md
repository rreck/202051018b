```json
{
  "id": "0fd96c787cb68c2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291845,
  "host_pid": "9e6742732c60:1",
  "hash": "2d25645eba70b559d5391a0e18d0d881f387a105e8f49a6db703eba9a1d1f8c3",
  "cid": "QmV12d25645eba70b559d5391a0e18d0d881f387a105",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291845,
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
      "evaluated_at": 1760291845
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
  "sig": "e9dc5bd1daf63d7d814d2c4d042449ccef4d594e9f1b091b0bf8645aab7222dd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159904059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 82595392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285764, 'matching_hash': '7ad1725ffd2dadfd'}}}