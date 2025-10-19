```json
{
  "id": "b43a7d2e4dc0de00",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291883,
  "host_pid": "9e6742732c60:1",
  "hash": "8b1449a81ab2ea676df9dc8f40a4775ea6d777127b35c07c81b14ed0ae92631f",
  "cid": "QmV18b1449a81ab2ea676df9dc8f40a4775ea6d77712",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291883,
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
      "evaluated_at": 1760291883
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
  "sig": "bf61c6a7437d80c33e18486c6253e1b17c2e91ea80a80208fa283d9caeea2bd1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598500621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 65973960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': '36e427bddf577026'}}}