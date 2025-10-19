```json
{
  "id": "eec87aef16afc51a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289798,
  "host_pid": "9e6742732c60:1",
  "hash": "1521c8f58d352d95c09d897b959052299fc82d6a15c7b0671503a5334395e1d3",
  "cid": "QmV11521c8f58d352d95c09d897b959052299fc82d6a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289798,
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
      "evaluated_at": 1760289798
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
  "sig": "4b2b7054b375b6e61dc270aee6b89a240594d380a43c75a9152351f0f28f997a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460644681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 45387979, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285764, 'matching_hash': '02c671505c0a8698'}}}