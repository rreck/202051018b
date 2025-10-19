```json
{
  "id": "0a94b587284a45f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290046,
  "host_pid": "9e6742732c60:1",
  "hash": "c8a1dddbf4d24a9308f16cfb63f7ed9c5d9fe633a0560a78faf85c9c41005ace",
  "cid": "QmV1c8a1dddbf4d24a9308f16cfb63f7ed9c5d9fe633",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290046,
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
      "evaluated_at": 1760290046
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
  "sig": "224577d0604d44b0229d227c490441a01164dd09325aa7ef465ff2ae78eca375"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154787030
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 61556600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285764, 'matching_hash': '945ae0d1ce138c7f'}}}