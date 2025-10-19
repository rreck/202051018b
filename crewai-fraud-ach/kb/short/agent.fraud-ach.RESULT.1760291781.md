```json
{
  "id": "8041d8ed31f5e106",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291781,
  "host_pid": "9e6742732c60:1",
  "hash": "0e331e41294f945da10df89ca7bc8154d00573e0edf3a80210942ec63729b23b",
  "cid": "QmV10e331e41294f945da10df89ca7bc8154d00573e0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291781,
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
      "evaluated_at": 1760291781
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
  "sig": "100930482948e3d8dfb167ff7a489ad0913354d2224d4fb4c0fa3bf4807e0d30"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039326834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 46865568, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': '4e66e6716d66a614'}}}