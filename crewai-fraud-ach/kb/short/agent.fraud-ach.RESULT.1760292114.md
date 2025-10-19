```json
{
  "id": "cb2698ad5b703502",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292114,
  "host_pid": "9e6742732c60:1",
  "hash": "1533dd76f2d47f8096dda2de6f7f77fd78f35a05729de82b33ccefc870471afa",
  "cid": "QmV11533dd76f2d47f8096dda2de6f7f77fd78f35a05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292114,
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
      "evaluated_at": 1760292114
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
  "sig": "e539235fd6a2c1dc62fc42b369c3818f5cb4c47e4a3685c1cef3b077d3fea591"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 52557230, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285765, 'matching_hash': 'a63e704272eccc25'}}}