```json
{
  "id": "785b7dcfe9cb168f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294325,
  "host_pid": "9e6742732c60:1",
  "hash": "4b28b9365daf0ee8c96b439d0751f33f0f0ce7802548e9db0188274d7903f2e1",
  "cid": "QmV14b28b9365daf0ee8c96b439d0751f33f0f0ce780",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294325,
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
      "evaluated_at": 1760294325
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
  "sig": "3c0af23e3658548806c0b388219d62b28f492836a0e3d6516b693deb2c8edd57"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152831142
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 47275520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'a7aa45f184f497a2'}}}