```json
{
  "id": "aed3b2a7e7e2fe4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294847,
  "host_pid": "9e6742732c60:1",
  "hash": "efad760de1b9089343b53829c167b353a4443aa2bb6349b7ec74720e00874f75",
  "cid": "QmV1efad760de1b9089343b53829c167b353a4443aa2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294847,
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
      "evaluated_at": 1760294847
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
  "sig": "d4301895a8d7fc7992acb07ae0ec326eb7486ffa4ad32b8f7b2f4910323c854c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020143117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 61250000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': '83c798d1c8d9cfec'}}}