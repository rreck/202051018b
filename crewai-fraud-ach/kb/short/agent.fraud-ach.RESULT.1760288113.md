```json
{
  "id": "212bc97c730b8aff",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288113,
  "host_pid": "9e6742732c60:1",
  "hash": "6632215ae9fe5006b74f4e1ba061b3e09f58d62fe477760d3042a9c58a20936d",
  "cid": "QmV16632215ae9fe5006b74f4e1ba061b3e09f58d62f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288113,
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
      "evaluated_at": 1760288113
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
  "sig": "6f1de0b4663f094e64e28ecc1101792ebe54344e80fdce6a629ebb54932f0bf7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460939533
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 27195614, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285763, 'matching_hash': '9fc2d1aa6be5a150'}}}