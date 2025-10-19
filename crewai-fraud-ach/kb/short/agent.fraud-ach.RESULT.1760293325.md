```json
{
  "id": "f5e6ec66d34cd3b1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293325,
  "host_pid": "9e6742732c60:1",
  "hash": "810b1a737f57339b05cda6e34936bd83dd5e36fd7616befd249177a5e9057ee7",
  "cid": "QmV1810b1a737f57339b05cda6e34936bd83dd5e36fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293325,
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
      "evaluated_at": 1760293325
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
  "sig": "862d8df0b71f06894099ee0c0f8e0707835eb3f15277cec2100bf397045e9bf2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 77920704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}