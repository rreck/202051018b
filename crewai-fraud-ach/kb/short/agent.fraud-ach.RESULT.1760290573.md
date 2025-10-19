```json
{
  "id": "b4ffa4f8e557eef9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290573,
  "host_pid": "9e6742732c60:1",
  "hash": "610d6e10e5050c35b01af8eed509f5f3026e828966ef9e1eb944f297177ae3a2",
  "cid": "QmV1610d6e10e5050c35b01af8eed509f5f3026e8289",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290573,
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
      "evaluated_at": 1760290573
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
  "sig": "645c88dae40e6da56f32ad7d70e67229907898aafd76b77b905036dda97012f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241272290
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 26540976, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285763, 'matching_hash': 'ac7868cb6249fe41'}}}