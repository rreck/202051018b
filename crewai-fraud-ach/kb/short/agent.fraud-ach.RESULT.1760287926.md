```json
{
  "id": "17b98df62ed3efcd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287926,
  "host_pid": "9e6742732c60:1",
  "hash": "aba24d82613aa08acc060244b1213fd55dabf66c42699c13eeb859be4347f890",
  "cid": "QmV1aba24d82613aa08acc060244b1213fd55dabf66c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287926,
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
      "evaluated_at": 1760287926
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
  "sig": "d5446e15ffca39e9e473de655771d036a94b472d1402cb083ce9c988babfc991"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022866819
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285763, 'matching_hash': '7f3c5046f4bcc1d0'}}}een': 1760285763, 'matching_hash': '9b2dabf2ca05df4f'}}}