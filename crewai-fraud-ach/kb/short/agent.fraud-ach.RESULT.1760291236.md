```json
{
  "id": "353e5b9c01891cf3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291236,
  "host_pid": "9e6742732c60:1",
  "hash": "22838704447dc93dcd56e7630b0c996fd3cf7c8fd38a37ce629c8b7613c1c588",
  "cid": "QmV122838704447dc93dcd56e7630b0c996fd3cf7c8f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291236,
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
      "evaluated_at": 1760291236
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
  "sig": "f262ab1e9c811533c66ab52c06ecbde881e71128d2a25d554f2d09ffcc4804b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464924143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 99970710, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760284979, 'matching_hash': '7b94effc1b7c4489'}}}