```json
{
  "id": "a9f1fd0c687f067b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288859,
  "host_pid": "9e6742732c60:1",
  "hash": "1cc8c46a084e0f0ed91f7f5ea31cc85a3758324f937fe0d4b41af98867b1cbc6",
  "cid": "QmV11cc8c46a084e0f0ed91f7f5ea31cc85a3758324f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288859,
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
      "evaluated_at": 1760288859
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
  "sig": "cccf7f1c5d59843044587428a9cda93f9678d5a0fbfbeed1929fdb1ef7ca7476"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246112063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 14712588, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '58be5dc306b57ee9'}}}