```json
{
  "id": "96cd72681078087d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292285,
  "host_pid": "9e6742732c60:1",
  "hash": "1f5b640e223db7f65ba421f05291a5ab8d60ab39554b32b01036e2297b44a3b5",
  "cid": "QmV11f5b640e223db7f65ba421f05291a5ab8d60ab39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292285,
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
      "evaluated_at": 1760292285
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
  "sig": "01105638b5e4d9790ad769913387719ab2fc9052cd3c5e4cb90a08fcf1f77a92"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152729668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 27207724, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': 'e33e77be4df2721a'}}}}