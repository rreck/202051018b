```json
{
  "id": "d37572b872b7f162",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291208,
  "host_pid": "9e6742732c60:1",
  "hash": "8262bffbfe2fb9576e4759b270a92dec2d2a810da2dc7b1f0e06b91a7b10a54e",
  "cid": "QmV18262bffbfe2fb9576e4759b270a92dec2d2a810d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291208,
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
      "evaluated_at": 1760291208
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
  "sig": "722ec7a76af46c8952d95c69c7b3741b55b7693b821a01ee3b45e38130d6c126"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596082317
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 65105560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285765, 'matching_hash': '7a1c6367235ff38a'}}}