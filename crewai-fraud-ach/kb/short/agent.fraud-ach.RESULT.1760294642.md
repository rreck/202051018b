```json
{
  "id": "e79d937534bb6e0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294642,
  "host_pid": "9e6742732c60:1",
  "hash": "3d3423361acda5a2ed0015cbe6e54c6266ab518100d460a64e0a156973c08f10",
  "cid": "QmV13d3423361acda5a2ed0015cbe6e54c6266ab5181",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294642,
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
      "evaluated_at": 1760294642
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
  "sig": "52424c3f15e91ecc0373dff92b039ed9a1bff9eca7b7790d32f65dc12aa4fe72"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249862639
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 83239530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '8cd9f1a7b8ce269f'}}}maly': {'fraud_detected': True, 'risk_score': 85, 'details': {'zscore': 4.56, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8725948}}}