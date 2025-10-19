```json
{
  "id": "09cbdc7cdad14af0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291633,
  "host_pid": "9e6742732c60:1",
  "hash": "13945fcd2b812dcc225cbc4ce799cce2563b5b58ee6c323d86df92709c6f6ecc",
  "cid": "QmV113945fcd2b812dcc225cbc4ce799cce2563b5b58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291633,
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
      "evaluated_at": 1760291633
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
  "sig": "918de32165da6243ac55a1815a499e56c276a4a48cfd8c38e98de98ef251651d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249334487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 37572816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285765, 'matching_hash': 'f464ac6512a738da'}}}