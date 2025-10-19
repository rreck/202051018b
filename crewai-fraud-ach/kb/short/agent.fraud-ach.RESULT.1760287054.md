```json
{
  "id": "b7a1e699627af830",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287054,
  "host_pid": "9e6742732c60:1",
  "hash": "9b620d28cba93ef9346f5824d948b8e3e138b641960a837c5ab92908619d78ab",
  "cid": "QmV19b620d28cba93ef9346f5824d948b8e3e138b641",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287054,
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
      "evaluated_at": 1760287054
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
  "sig": "cd64ed2d35d0b71b279c8feb74bd16d4038a848bc77ed275dd8687e467bd39aa"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14639408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}