```json
{
  "id": "a0dc80e8f0d1427e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287533,
  "host_pid": "9e6742732c60:1",
  "hash": "cad59051f17bb98ebd2fa98b51b6948d7d5a0f6444a65dc51fde4b1651be4203",
  "cid": "QmV1cad59051f17bb98ebd2fa98b51b6948d7d5a0f64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287533,
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
      "evaluated_at": 1760287533
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
  "sig": "3f7faa5e96226f757a0a6796ae7dd731c4c7e5b6dc245a5f8967b38f629b5ee2"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 20049624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}