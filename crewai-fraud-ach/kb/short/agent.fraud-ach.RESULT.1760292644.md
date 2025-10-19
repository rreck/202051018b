```json
{
  "id": "268c8ae4d96cd0e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292644,
  "host_pid": "9e6742732c60:1",
  "hash": "4af4baa9c363c1830bbf93b32fb249144470b80aca147435bc33684a4d4635b1",
  "cid": "QmV14af4baa9c363c1830bbf93b32fb249144470b80a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292644,
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
      "evaluated_at": 1760292644
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
  "sig": "2bbc40bd912c35a5bb5843a28b5a5cf5a5d0c85b24f465000abe5a038e22bb6f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463060709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 95895662, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285764, 'matching_hash': '9043a83188003850'}}}