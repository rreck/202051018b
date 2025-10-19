```json
{
  "id": "b62a3cbfce704064",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291501,
  "host_pid": "9e6742732c60:1",
  "hash": "655283b6b8cb6b9ecb480d782d8dfe3d9c582ceea74c965bf1f5cafc5e3e2b49",
  "cid": "QmV1655283b6b8cb6b9ecb480d782d8dfe3d9c582cee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291501,
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
      "evaluated_at": 1760291501
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
  "sig": "2baee711512210778a106c11a4c091b661590c193ac08be8d72970eee88b3d48"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029278927
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 176, 'threshold': 50, 'total_amount': 50859424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 175, 'first_seen': 1760285765, 'matching_hash': '45338af8ff50831c'}}}