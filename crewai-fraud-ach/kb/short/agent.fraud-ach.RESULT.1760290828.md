```json
{
  "id": "0747e3fe1f63a030",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290828,
  "host_pid": "9e6742732c60:1",
  "hash": "55f1f6dacff5525a00619ea5fd69ba53594cdd5c370f0beb727cd86f669733f3",
  "cid": "QmV155f1f6dacff5525a00619ea5fd69ba53594cdd5c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290828,
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
      "evaluated_at": 1760290828
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
  "sig": "f694173ce5db37a3d434afe5dc1b642527b81b2160ce05e9917032bce1b70928"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244317854
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 60731200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285765, 'matching_hash': '3595d612a0391b5c'}}}