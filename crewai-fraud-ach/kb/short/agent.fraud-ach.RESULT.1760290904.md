```json
{
  "id": "f6f46948ff2a0fb4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290904,
  "host_pid": "9e6742732c60:1",
  "hash": "80d3d88a095242575a4905a2fe3f120fbe571b7c35a0c4981d16d71ecb45e7b4",
  "cid": "QmV180d3d88a095242575a4905a2fe3f120fbe571b7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290904,
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
      "evaluated_at": 1760290904
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
  "sig": "05f0e1f57ee512cf85a4b57531d0214517b4b97d04b9b38c4cf8c6ad8c2b4ea4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026169646
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 48281508, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285764, 'matching_hash': '09339571c5d51c89'}}}