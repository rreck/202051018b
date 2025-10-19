```json
{
  "id": "457cd7c3dda236e6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289727,
  "host_pid": "9e6742732c60:1",
  "hash": "7f37910e2c89e25f129281c3f167750afd075e16c3e453db66d1ae583e0ac60c",
  "cid": "QmV17f37910e2c89e25f129281c3f167750afd075e16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289727,
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
      "evaluated_at": 1760289727
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
  "sig": "c23e94697d4e80b241394b95f1acc4ac9183bd6235cb640fd2a95353a6c6bbee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029964192
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 39746055, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285764, 'matching_hash': '3fa9c762fe00e5a2'}}}