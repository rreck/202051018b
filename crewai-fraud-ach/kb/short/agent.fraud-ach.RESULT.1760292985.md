```json
{
  "id": "e36a8276fc93d8c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292985,
  "host_pid": "9e6742732c60:1",
  "hash": "d782e1dcec2005e46c1b7660b5576d7ed9912165cb8fce92c617cf68613d8377",
  "cid": "QmV1d782e1dcec2005e46c1b7660b5576d7ed9912165",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292985,
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
      "evaluated_at": 1760292985
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
  "sig": "88019542a4d9fa114a56ae401eddef382f80293f0699c4cc7456d3fa477a263e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465280061
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 27796582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '24e243e35a5cb5f6'}}}