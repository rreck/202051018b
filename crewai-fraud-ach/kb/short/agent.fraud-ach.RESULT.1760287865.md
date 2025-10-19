```json
{
  "id": "fa4b42dd0a06512c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287865,
  "host_pid": "9e6742732c60:1",
  "hash": "32754ed4965be115decbc3640b352a5f2b23c977dad3ad0892b839342d6c97c5",
  "cid": "QmV132754ed4965be115decbc3640b352a5f2b23c977",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287865,
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
      "evaluated_at": 1760287865
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
  "sig": "7a046af3477ff803b95aa26eb5abcb6b5de7bce7bbd661d5a4ecef1ad99bf8fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591752071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285763, 'matching_hash': 'afb8628b94bcbefe'}}}