```json
{
  "id": "420fc5352612eba8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294644,
  "host_pid": "9e6742732c60:1",
  "hash": "de3646c8754d2dd59f3241bc61c97a2ecee86940ed53e333bdbc65c56a79bf46",
  "cid": "QmV1de3646c8754d2dd59f3241bc61c97a2ecee86940",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294644,
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
      "evaluated_at": 1760294644
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
  "sig": "326b6a62f0942e7894eee7664abbaa03f511834766de89e0e72dd738a73c0321"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155093747
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 60500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '733cbbfa8b499b66'}}}