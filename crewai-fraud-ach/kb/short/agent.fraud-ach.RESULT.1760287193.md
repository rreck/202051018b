```json
{
  "id": "562083df19c131a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287193,
  "host_pid": "9e6742732c60:1",
  "hash": "3ee73d38c0ac9c180675942cba6e1143b4ae0785b130360bedbe23eaf76809db",
  "cid": "QmV13ee73d38c0ac9c180675942cba6e1143b4ae0785",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287193,
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
      "evaluated_at": 1760287193
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "60b38263b34bd7b6e89da2c96654fdd987e63d0bf784f24878f05ff4a03f4fdb"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 17055828, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}