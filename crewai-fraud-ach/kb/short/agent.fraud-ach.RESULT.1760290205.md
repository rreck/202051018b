```json
{
  "id": "223317123ca989a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290205,
  "host_pid": "9e6742732c60:1",
  "hash": "45f99d631673121d396262a09a76844e6de3645fce8cfa554dcfc1de39a0195b",
  "cid": "QmV145f99d631673121d396262a09a76844e6de3645f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290205,
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
      "evaluated_at": 1760290205
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
  "sig": "2a3e24dc1d985b83632c5b829086b144dbb0fb299d91b880b4cc7479d5d4022c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039486184
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 90689060, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760284979, 'matching_hash': '923cee7332714d41'}}}