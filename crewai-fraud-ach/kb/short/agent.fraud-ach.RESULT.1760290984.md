```json
{
  "id": "78d5088970180479",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290984,
  "host_pid": "9e6742732c60:1",
  "hash": "e4b03df14a40d3a0b034bc510185f860a5bf38b005b77d243ed620208229fc7e",
  "cid": "QmV1e4b03df14a40d3a0b034bc510185f860a5bf38b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290984,
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
      "evaluated_at": 1760290984
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
  "sig": "9377882187bff23ab1c3c96557c46806acba3ec6c5d27b892ec68e20fd37a4a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158715464
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 24301684, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': '08e14bce24e2b1ea'}}}