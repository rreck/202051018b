```json
{
  "id": "77ad29b1a9f29b5d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294563,
  "host_pid": "9e6742732c60:1",
  "hash": "c4f6dea24df3d89af52066d0d72bf3f04fa945bfc1805b1b5690fc9351287fc9",
  "cid": "QmV1c4f6dea24df3d89af52066d0d72bf3f04fa945bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294563,
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
      "evaluated_at": 1760294563
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
  "sig": "e64db4b53e2a2eb8cd83fce76e20f38454376f3c64549b1acf89a172d413af35"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158219859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 101656560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': '5fa0c304c44ad0bf'}}}