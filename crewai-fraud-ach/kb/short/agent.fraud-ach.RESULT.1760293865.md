```json
{
  "id": "efcac1549d848846",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293865,
  "host_pid": "9e6742732c60:1",
  "hash": "673f1b9e3e3d02220b7cd49346d99955df30061d80ba4fb3801c6c9c17c51be8",
  "cid": "QmV1673f1b9e3e3d02220b7cd49346d99955df30061d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293865,
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
      "evaluated_at": 1760293865
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
  "sig": "56db3cb9b42ec173ae0035b78914df89e5fdd82f9af07838c55c3e867628bb2d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276179264
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 38920512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': 'cb2614db0e970d70'}}}