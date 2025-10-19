```json
{
  "id": "a4273982448b9ae3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288860,
  "host_pid": "9e6742732c60:1",
  "hash": "7e20e856ab880a2872304ecc88a8fea6fe1d6f97cbcf172c77ff1e695cee0ddd",
  "cid": "QmV17e20e856ab880a2872304ecc88a8fea6fe1d6f97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288860,
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
      "evaluated_at": 1760288860
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
  "sig": "5bbb93b7550239fe10665bf5731e82ff1ee40b311d2dcbcfcb45755a7db55282"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240849779
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 20473370, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '760b7e67ac1502b4'}}}