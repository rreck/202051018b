```json
{
  "id": "6b1989c399e5c690",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294538,
  "host_pid": "9e6742732c60:1",
  "hash": "9daae1189dcb03a92ac0770db04981fe847e39e4b5c2badcb6bda00a2467dcd1",
  "cid": "QmV19daae1189dcb03a92ac0770db04981fe847e39e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294538,
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
      "evaluated_at": 1760294538
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
  "sig": "f01d1a5b3d1b0d4a940c0552feeab17488fc73e8a694ad2b84ebd7ecd7849dd7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022866819
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 24000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '7f3c5046f4bcc1d0'}}}