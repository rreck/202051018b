```json
{
  "id": "26d906a89a3516a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291251,
  "host_pid": "9e6742732c60:1",
  "hash": "c62ac3994c1bf6cd950247ef0d530c192ca34f647dbffe8088fdc90a049d8752",
  "cid": "QmV1c62ac3994c1bf6cd950247ef0d530c192ca34f64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291251,
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
      "evaluated_at": 1760291251
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
  "sig": "e772e27274dcdcc7cebab1d2e9b78d44f37d1a816b123740eec898d0272c5ce1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 54102160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}