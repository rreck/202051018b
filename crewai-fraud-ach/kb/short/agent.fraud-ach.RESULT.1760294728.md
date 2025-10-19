```json
{
  "id": "6844b6597f03751d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294728,
  "host_pid": "9e6742732c60:1",
  "hash": "ee23e3b47d4079caaad3f13f84fd32f5a37725e13885f691096ca140c9b94293",
  "cid": "QmV1ee23e3b47d4079caaad3f13f84fd32f5a37725e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294728,
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
      "evaluated_at": 1760294728
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
  "sig": "9836143586eaf601cfe37ea64891cf08a3221c783fa96cc1a6539970a9056d0d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464452578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 23402601, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285764, 'matching_hash': '0a8d6c8cd4d67655'}}}