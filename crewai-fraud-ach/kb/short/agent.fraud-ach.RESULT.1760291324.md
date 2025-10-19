```json
{
  "id": "d7637a733d1b3ce2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291324,
  "host_pid": "9e6742732c60:1",
  "hash": "30b1d507b3df02e9b10295f68ccd8dad8c4604b8788111bcc22630c174cf9233",
  "cid": "QmV130b1d507b3df02e9b10295f68ccd8dad8c4604b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291324,
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
      "evaluated_at": 1760291324
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
  "sig": "b061d64ae4a4bc55e9569fef46a5843556353a8708e2320647ef7cfca20e08b9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599017181
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 30478056, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '7f94592234367703'}}}