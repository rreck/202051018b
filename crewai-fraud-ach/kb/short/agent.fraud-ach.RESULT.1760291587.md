```json
{
  "id": "f2d6ddcadb74ada2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291587,
  "host_pid": "9e6742732c60:1",
  "hash": "3fb9b853f327fbff8a153f644a071e53beb63afa4a3efa2b04fc9357a2d01632",
  "cid": "QmV13fb9b853f327fbff8a153f644a071e53beb63afa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291587,
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
      "evaluated_at": 1760291587
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
  "sig": "02757b02e9f42f3206482ec829a0781c56c05891d4bce2f6a9a43385535b6b0c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025341515
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 44721432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': '76c6a410184ad94b'}}}