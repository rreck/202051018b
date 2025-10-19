```json
{
  "id": "3b310dbbe652e213",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291922,
  "host_pid": "9e6742732c60:1",
  "hash": "75bd94f469ca73d9fc128bf2556a3086c4da7596d1e6e16c07c0e36854663faa",
  "cid": "QmV175bd94f469ca73d9fc128bf2556a3086c4da7596",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291922,
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
      "evaluated_at": 1760291922
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
  "sig": "bffc7ecd1a8aef149aef44f230c4b74e3a194302f965677596989a9d1a5bc735"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021173532
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 57338034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': 'a0cc7134a86fdd26'}}}