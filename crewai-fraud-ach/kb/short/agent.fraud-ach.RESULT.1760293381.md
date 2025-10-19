```json
{
  "id": "8c7080e1d2332dc0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293381,
  "host_pid": "9e6742732c60:1",
  "hash": "dd9f735ef73de1e1ef9ae3ee718360c82d8ac8ac7a24b791e4981ca17f52b1b8",
  "cid": "QmV1dd9f735ef73de1e1ef9ae3ee718360c82d8ac8ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293381,
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
      "evaluated_at": 1760293381
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
  "sig": "fe508262a6b8b14880bcb89e04d151259212e8d0dd805e582c8c00bf07c3f7bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279280277
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 95854325, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '5e64cdd29eaed333'}}}