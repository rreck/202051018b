```json
{
  "id": "d4c285831bb85960",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289036,
  "host_pid": "9e6742732c60:1",
  "hash": "7cdb29f69b606f791326fceb8193fd96d4cf5ac8946a180c51a84829943e727f",
  "cid": "QmV17cdb29f69b606f791326fceb8193fd96d4cf5ac8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289036,
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
      "evaluated_at": 1760289036
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
  "sig": "c1eb15386449a72cc315d96619408fe1e6ab7468af3bdf602aa2a1cd5492acac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021480535
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 54750417, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285765, 'matching_hash': '9682be52dcbb3d1d'}}}