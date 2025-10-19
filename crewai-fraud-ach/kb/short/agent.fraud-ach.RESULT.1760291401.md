```json
{
  "id": "6c85e8799b9d3a73",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291401,
  "host_pid": "9e6742732c60:1",
  "hash": "4be8310b0fd88770404e99434c70ecf2af8ef4df7980118a9f70ce813a80d0d1",
  "cid": "QmV14be8310b0fd88770404e99434c70ecf2af8ef4df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291401,
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
      "evaluated_at": 1760291401
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
  "sig": "21243165eddbc2c0ed1745152e3231cf483dbf99be0ce71c33c942aa4815421f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595557022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 82820694, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285764, 'matching_hash': '3443c05f2ecc9733'}}}