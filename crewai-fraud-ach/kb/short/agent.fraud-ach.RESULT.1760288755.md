```json
{
  "id": "1cdd3d9077abc3f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288755,
  "host_pid": "9e6742732c60:1",
  "hash": "e4b53cdb44f506015e8cead3bdf7f25caa96f2756eceb5359864488b69a79b60",
  "cid": "QmV1e4b53cdb44f506015e8cead3bdf7f25caa96f275",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288755,
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
      "evaluated_at": 1760288755
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
  "sig": "c28cbc739bdc6b1420a206d63c218ad6953031a67aef719978f8f36a3b1578ae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038318648
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 32968034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285765, 'matching_hash': '13d51597e8ec53d0'}}}