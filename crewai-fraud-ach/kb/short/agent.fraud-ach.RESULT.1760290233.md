```json
{
  "id": "494ef69975f035d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290233,
  "host_pid": "9e6742732c60:1",
  "hash": "fad670eaeb4dfc45363fcd8a6f5da6a76eb8191dfa38a586dfe0e3c48fb3acef",
  "cid": "QmV1fad670eaeb4dfc45363fcd8a6f5da6a76eb8191d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290233,
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
      "evaluated_at": 1760290233
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
  "sig": "e448920bd46683fd189ff95975c4d38f3de4c10b058d163e6acc9939721c241a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468298709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': '7ee51499d35b3ada'}}}