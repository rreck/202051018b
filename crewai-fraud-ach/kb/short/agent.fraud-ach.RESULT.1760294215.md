```json
{
  "id": "3fc00bcc1f5879f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294215,
  "host_pid": "9e6742732c60:1",
  "hash": "71350096f91bccfcc0122b057a4dc8e00d89c8d1171ac361863b922c9f82a3d1",
  "cid": "QmV171350096f91bccfcc0122b057a4dc8e00d89c8d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294215,
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
      "evaluated_at": 1760294215
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
  "sig": "2b0539d684a63c4d539bdbecb3d840d8e2a18980955783a9092de9e3da294f60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024544859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 113423076, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': '21e0fdbcd06f2d49'}}}