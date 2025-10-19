```json
{
  "id": "da341d2ff1993f83",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291419,
  "host_pid": "9e6742732c60:1",
  "hash": "39e45f4995a5e33423b70372e9dddeafdf3b0311957f2728901377b45b358cfc",
  "cid": "QmV139e45f4995a5e33423b70372e9dddeafdf3b0311",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291419,
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
      "evaluated_at": 1760291419
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
  "sig": "3983ca5a412d73afb06efa2ba747247fbe5b80101b623740016f50b419c4ec7d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155958228
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 73348308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285765, 'matching_hash': '1e57f627a6d207f5'}}}